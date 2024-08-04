/** A button that plays a specific song.  */
export function Button({
  label,
  songLink,
}: {
  label: string;
  songLink: string;
}) {
  return (
    <button
      style={{
        backgroundColor: "blue",
        color: "white",
        padding: "10px",
        margin: "10px",
        borderRadius: "5px",
        border: "none",
        cursor: "pointer",
      }}
      onClick={async () => {
        const response = await fetch(`http://localhost:8000/song/${songLink}`);

        console.log(JSON.stringify(response));

        if (!response.ok) {
          throw new Error(
            "Failed to play song.\nReason: " + response.statusText
          );
        }

        return;
      }}
    >
      {label}
    </button>
  );
}
