const DEFAULT_STEP_SIZE: f64 = 0.001;

// ---------------------- //
// -- Public Interface -- //
// ---------------------- //

/// Integrates a callable function.
pub fn integrate<F>(callable: F, domain: (f64, f64), dx: Option<f64>) -> f64
where
    F: Fn(f64) -> f64,
{
    // Unpack args
    let (left, right) = domain;
    let dx = dx.unwrap_or(DEFAULT_STEP_SIZE);

    // Setup loop variables
    let mut total: f64 = 0.0;
    let mut x = left;

    // Iteratively integrate (LHS Riemann sum)
    while x < right {
        let dy = callable(x) * dx;
        total += dy;
        x += dx;
    }

    // Return computed total
    total
}

// ----------- //
// -- Tests -- //
// ----------- //

#[cfg(test)]
mod tests {
    use super::*;

    /// Percentage difference we tolerate to consider two values equal
    const ACCEPTABLE_PRECISION: f64 = 0.05;

    /// Helper function to verify that the two values are approximately equal.
    fn approx_equal(a: f64, b: f64) -> bool {
        let diff = (a - b).abs();
        let average_value = (a + b).abs() / 2.0;
        let percentage_diff = diff / average_value;

        dbg!(percentage_diff);

        percentage_diff < ACCEPTABLE_PRECISION
    }

    #[test]
    /// Verifies that our uniform integral matches our expectations
    fn test_uniform_integral() {
        let result = integrate(|_x: f64| 1.0, (0.0, 10.0), None);
        let expected = 10.0;
        assert!(approx_equal(result, expected));
    }

    #[test]
    /// Verifies that our linear integral matches our expectations
    fn test_linear_integral() {
        let result = integrate(|x: f64| x, (0.0, 10.0), None);
        let expected = 50.0;

        assert!(approx_equal(result, expected));
    }

    #[test]
    /// Verify that the e^(-x) integral is 0 between (0, ∞)
    fn test_exponential_integral() {
        let result = integrate(|x: f64| (-x).exp(), (0.0, 1e5), None);
        let expected = 1.0;
        assert!(approx_equal(result, expected));
    }

    #[test]
    /// Verifies that the integral is consistent across different step sizes.
    fn test_consistency_in_dx() {
        let callable = |x: f64| x * x;
        let domain = (0.0, 100.0);

        let expected = integrate(callable, domain, None);

        for dx in [1.0, 0.1, 0.01, 0.001, 0.0001].iter() {
            let result = integrate(callable, domain, Some(*dx));
            assert!(approx_equal(result, expected));
        }
    }
}
