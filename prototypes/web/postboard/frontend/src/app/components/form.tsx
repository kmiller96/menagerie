import styles from "./form.module.css"

/** Defines the submission form */
export default function SubmissionForm() {
	return (
		<div className={styles.form}>
			<form>
				<div>
					<textarea id="content" />
				</div>
				<div>
					<input type="text" id="author" />
				</div>
				<div>
					<input type="submit" id="submit" />
				</div>
			</form>
		</div>
	)
}