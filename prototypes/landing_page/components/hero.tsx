export function Hero() {
  return (
    <div
      className="hero min-h-screen"
      style={{
        backgroundImage:
          "url(/dog-walking.webp), linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5))",
      }}
    >
      <div className="hero-overlay bg-opacity-80"></div>
      <div className="hero-content h-full w-full flex flex-col justify-between">
        <h1 className="text-6xl md:text-8xl self-start">
          Let Your Dog Walk Themselves
        </h1>
        <h2 className="text-3xl self-end md:max-w-[40%] text-end">
          Automate your dog walking business
        </h2>
      </div>
    </div>
  );
}
