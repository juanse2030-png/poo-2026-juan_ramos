fn main() {
    let nombre = "Bro";
    let edad = 20;
    let lenguaje = "Rust";

    println!("Hola, {} 👋", nombre);
    println!("Tienes {} años.", edad);
    println!("Estás aprendiendo {}.", lenguaje);

    let a = 10;
    let b = 5;
    let suma = a + b;

    println!("La suma de {} + {} = {}", a, b, suma);

    if suma > 10 {
        println!("El resultado es mayor que 10.");
    } else {
        println!("El resultado es 10 o menor.");
    }
}