use yew::prelude::*;
use yew::Properties;

use postboard_structs::Post;

#[derive(Properties, PartialEq)]
pub struct Props {
    pub posts: Vec<Post>,
}

#[function_component]
pub fn Feed(props: &Props) -> Html {
    let posts = props
        .posts
        .iter()
        .map(|post| html! {<p> {format!("{}", post)} </p>})
        .collect::<Html>();

    html! {
        <div> { posts } </div>
    }
}
