const data = [
  { id: 1, name: "John Doe" },
  { id: 2, name: "Jane Doe" },
  { id: 3, name: "Alice" },
  { id: 4, name: "Bob" },
];

const error = { detail: "Unauthorized" };

/** Mocked function that retrieves data from an API.
 *
 * If there is no token in the local storage, it will return a mocked 401 status
 * code as if the user is unauthorized.
 */
export async function useAPI(): Promise<Response> {
  const token = localStorage.getItem("token");

  const response = token
    ? Response.json(data, { status: 200 })
    : new Response(JSON.stringify(error), { status: 401 });

  console.log(response);
  return new Promise(() => response);
}
