use yew::prelude::*;

use gloo::{console::log, utils::document};

#[function_component]
pub fn PostForm() -> Html {
    let content = use_state(|| String::from(""));

    let onchange = Callback::from(|e: Event| {
        let target = e.target();
        log!(target);
    });

    let onsubmit = {
        Callback::from(move |e: SubmitEvent| {
            e.prevent_default();
        })
    };

    html! {
        <form {onsubmit}>
            <input type="textarea" id="content" {onchange} />
            <br />
            <input type="submit" value="Submit" id="submit" />
        </form>
    }
}
