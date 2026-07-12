use numerical_integral::integrate;

fn main() {
    let result = integrate(|x| x * x, (0.0, 10.0), None);
    println!("Result: {}", result);
}
