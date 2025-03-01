"use client";

import { useEffect } from "react";

import { Terminal as XTerm } from "@xterm/xterm";
import "@xterm/xterm/css/xterm.css";

export function Terminal() {
  useEffect(() => {
    // Initialise xterm
    const container = document.getElementById("terminal")!;
    const xterm = new XTerm({
      cursorBlink: true,
    });
    xterm.open(container);

    // Handlers
    xterm.onKey((e) => {
      console.log(e.key);

      if (e.key === "\r") {
        xterm.writeln("");
        return;
      } else {
        xterm.write(e.key);
      }
    });

    // Focus
    xterm.focus();
  }, []);

  return <div id="terminal" className="w-screen h-screen"></div>;
}
