import { useState } from "react";

export function useLocalStorage<T>(key: string, defaultValue: T) {
  // -- Hook State -- //
  const [value, setValue] = useState(() => {
    try {
      const stored = window.localStorage.getItem(key);
      if (stored) {
        return JSON.parse(stored);
      } else {
        window.localStorage.setItem(key, JSON.stringify(defaultValue));
        return defaultValue;
      }
    } catch (error) {
      return defaultValue;
    }
  });

  // -- Hook Setter -- //
  const setter = (newValue: T) => {
    try {
      window.localStorage.setItem(key, JSON.stringify(newValue));
    } catch (error) {
      console.error(error);
    }
    setValue(newValue);
  };

  // -- Return -- //
  return [value, setter];
}
