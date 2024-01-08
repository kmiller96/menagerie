//! Defines the main application.

use postboard_structs::Post;
use yew::prelude::*;

use crate::components::{feed, form, heading};

fn make_test_data() -> Vec<Post> {
    let post1 = Post::new(None, String::from("Post #1"));
    let post2 = Post::new(None, String::from("Post #2"));

    vec![post1, post2]
}

#[function_component]
pub fn App() -> Html {
    html! {
    <>
        <heading::Heading />
        <form::PostForm />
        <feed::Feed posts={make_test_data()}/>
    </>
    }
}
