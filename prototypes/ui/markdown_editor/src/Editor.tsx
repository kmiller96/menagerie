export function Editor({
  content,
  setContent,
}: {
  content: string;
  setContent: (content: string) => void;
}) {
  return (
    <div
      style={{
        padding: "10px 10px",
        flexGrow: 1,
      }}
    >
      <textarea
        style={{
          width: "100%",
          height: "100%",
          border: "none",
          overflow: "auto",
          outline: "none",
          resize: "none",
        }}
        value={content}
        onChange={(e) => setContent(e.target.value)}
      />
    </div>
  );
}
