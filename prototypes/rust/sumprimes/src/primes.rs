//! Defines the prime utilities

// Sums N primes.
pub fn sum_primes(n: &usize) -> usize {
    let top_bound = estimate_upper_bound(&n);

    let primes: Vec<usize> = primes_below(&(top_bound + 1));
    let primes = primes.iter().take(*n);

    primes.sum()
}

// Estimates the top bound for the sieve of eratosthenes
fn estimate_upper_bound(n: &usize) -> usize {
    let n = *n as f64;

    let estimate = (n * (n * n.ln()).ln()) as usize;
    let min = 10; // HACK: Failsafe for very small values of n

    std::cmp::max(estimate, min)
}

// Returns the list of primes below the supplied value
fn primes_below(n: &usize) -> Vec<usize> {
    let n = *n;

    // Setup the vectors in the sieve
    let mut numbers: Vec<usize> = (0..n).collect();
    let mut is_prime = vec![true; (n + 1) as usize];

    is_prime[0] = false; // 0 =/= prime
    is_prime[1] = false; // 1 =/= prime

    // Determine hault condition
    let max_p = (n as f64).sqrt() as usize;

    // Iterate through values `p` until p <= max
    let mut p: usize = 2;
    while p <= max_p {
        if is_prime[p] {
            let mut mul = 2;
            let mut pp = p * mul;

            while pp < (n as usize) {
                is_prime[pp] = false;

                mul += 1;
                pp = p * mul;
            }
        }

        p += 1
    }

    // Only keep the primes
    let mut iter = is_prime.iter();
    numbers.retain(|_| *iter.next().unwrap());

    // Return the primes
    numbers
}

#[cfg(test)]
mod tests {

    #[test]
    fn estimate_upper_bound_first_2_primes() {
        // 2nd prime == 3, so should be this or greater
        assert!(dbg!(super::estimate_upper_bound(&2)) >= 3);
    }

    #[test]
    fn estimate_upper_bound_first_10_primes() {
        // 10th prime == 29, so should be this or greater
        assert!(super::estimate_upper_bound(&10) >= 29);
    }

    #[test]
    fn estimate_upper_bound_first_100_primes() {
        // 100th prime == 541, so should be this or greater
        assert!(super::estimate_upper_bound(&100) >= 541);
    }

    #[test]
    fn primes_below_5() {
        assert_eq!(super::primes_below(&5), vec![2, 3])
    }

    #[test]
    fn primes_below_10() {
        assert_eq!(super::primes_below(&10), vec![2, 3, 5, 7])
    }

    #[test]
    fn primes_below_50() {
        assert_eq!(
            super::primes_below(&50),
            vec![2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        )
    }

    #[test]
    fn sum_primes_first_3() {
        assert_eq!(super::sum_primes(&3), 10)
    }

    #[test]
    fn sum_primes_first_10() {
        assert_eq!(super::sum_primes(&10), 129)
    }

    #[test]
    fn sum_primes_first_1000() {
        assert_eq!(super::sum_primes(&1000), 3682913)
    }
}
