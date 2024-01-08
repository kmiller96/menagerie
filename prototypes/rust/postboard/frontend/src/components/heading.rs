//! Defines the heading of the application

use yew::prelude::*;

#[function_component]
pub fn Heading() -> Html {
    html! {
        <h1>{ "Postboard" }</h1>
    }
}
