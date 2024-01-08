use yew::prelude::*;

#[function_component]
pub fn PostForm() -> Html {
    html! {
        <form method="POST" action="http://localhost:8000/api/post">
            <input type="textarea" id="content" />
            <input type="submit" value="Submit" id="submit" />
        </form>
    }
}
