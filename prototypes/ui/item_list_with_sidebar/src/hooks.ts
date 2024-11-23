export function useData() {
  return {
    data: [
      {
        id: "top_sales_reps",
        name: "Who is my top performing sales representative?",
      },
      {
        id: "working_capital",
        name: "How much money is tied up in inventory?",
      },
    ],
    error: null,
    isLoading: false,
  };
}
