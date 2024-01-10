import styles from "./form.module.css";

/** Defines the submission form */
export default function SubmissionForm() {
  return (
    <div className={styles.form}>
      <form>
        <div>
          <textarea
            id="content"
            autoCorrect="on"
            placeholder="What would you like to say?"
          />
        </div>
        <div>
          <input type="text" id="author" placeholder="Name (Optional)" />
        </div>
        <div>
          <input type="submit" id="submit" />
        </div>
      </form>
    </div>
  );
}
