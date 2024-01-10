import styles from "./feed.module.css"

/** A feed of posts by users.
 * 
 */
export default function Feed({ data }: { data: Array<{ author: string, content: string }> }) {
	return (
		<div className={styles.feed}>
			{data.map((post, i) => <FeedPost key={i} author={post.author} content={post.content} />)}
		</div>
	)
}

/** Individual feed post */
function FeedPost({ author, content }: { author: string, content: string }) {
	return (
		<div>
			<p><b>@{author}:</b> {content}</p>
		</div>
	)
}