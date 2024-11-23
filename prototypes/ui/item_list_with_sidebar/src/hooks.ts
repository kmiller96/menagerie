import { QUESTIONS } from "./data";

export function useData() {
  return {
    data: QUESTIONS,
    error: null,
    isLoading: false,
  };
}
