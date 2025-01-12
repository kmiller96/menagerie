import { Modal } from "@/components/modal";
import { ThemeToggle } from "@/components/themeToggle";

export default function Home() {
  return (
    <div className="flex justify-center items-center h-screen">
      <div className="flex flex-col w-6/12 gap-5 justify-center align-middle">
        <ThemeToggle />
        <Modal />
        <button className="btn btn-primary">I do nothing</button>
      </div>
    </div>
  );
}
