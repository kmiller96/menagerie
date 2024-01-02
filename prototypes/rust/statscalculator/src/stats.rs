//! Defines the statistical functions

// Computes the statistical information about the series
pub fn compute(series: &Vec<f64>) -> (f64, f64) {
    let mu = mean(series);
    let sigma = stddev(series, mu);

    (mu, sigma)
}

/// Computes the mean the series.
fn mean(series: &Vec<f64>) -> f64 {
    let sum = &series.into_iter().sum::<f64>();
    let count = &series.into_iter().count();

    sum / (*count as f64)
}

/// Computes the standard deviation of the series.
///
/// We require the mean to be explicitly passed in to remove the need to recompute
/// the value.
fn stddev(series: &Vec<f64>, mean: f64) -> f64 {
    let count: f64 = *(&series.into_iter().count()) as f64;
    let numerator: f64 = *(&series.into_iter().map(|x| (mean - x).powi(2)).sum::<f64>());

    (numerator / count).sqrt()
}
