"use client";

import { useEffect } from "react";

import { initTerminal } from "ttty";

export function Terminal() {
  useEffect(() => {
    const terminal = initTerminal({
      host: document.getElementById("terminal")!,
      prompt: "guest@kalemiller.com $ ",
      commands: {
        ls: {
          name: "ls",
          description: "List directory contents",
          func: (terminal) => {
            terminal.print("There is nothing here...");
          },
        },
        clear: {
          name: "clear",
          description: "Clear the terminal screen",
          func: (terminal) => {
            terminal.commandContainer.innerHTML = "";
          },
        },
      },
    });
  }, []);

  return (
    <div
      id="terminal"
      style={{
        width: "100vw",
        height: "50vh",
      }}
    ></div>
  );
}
