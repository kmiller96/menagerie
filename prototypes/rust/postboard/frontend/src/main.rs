use yew::prelude::*;

#[function_component]
fn App() -> Html {
    html! {
        <p>{ "Hello World!" } </p>
    }
}

fn main() {
    yew::Renderer::<App>::new().render();
}
