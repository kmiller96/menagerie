import { Button } from "./components/Button";

const SONGS = [
  {
    label: "Tie Fighter Death",
    songLink:
      "https://open.spotify.com/track/3HMYWUXaYCTar5k9nfMumn?si=20d258e42d26481c",
  },
  {
    label: "Duel of the Fates",
    songLink:
      "https://open.spotify.com/track/1ghlpxVfPbFH2jenrv9vVw?si=31168762b3634f02",
  },
];

export function App() {
  return (
    <div style={{ display: "flex", flexDirection: "column", padding: "10px" }}>
      {SONGS.map((song) => (
        <Button key={song.label} label={song.label} songLink={song.songLink} />
      ))}
    </div>
  );
}
