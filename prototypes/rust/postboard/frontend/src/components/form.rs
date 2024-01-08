use yew::prelude::*;

use gloo::console::log;

#[function_component]
pub fn PostForm() -> Html {
    let content = use_state(|| String::from(""));

    let on_input = {
        let content = content.clone();
        Callback::from(move |e: InputEvent| content.set(e.data().unwrap_or_default()))
    };

    let on_submit = {
        let content = content.clone();
        Callback::from(move |e: SubmitEvent| {
            e.prevent_default();
            log!(content.get(0..)) // HACK: I have no idea why I need to do this...
        })
    };

    html! {
        <form onsubmit={on_submit}>
            <input type="textarea" id="content" oninput={on_input} />
            <br />
            <input type="submit" value="Submit" id="submit" />
        </form>
    }
}
