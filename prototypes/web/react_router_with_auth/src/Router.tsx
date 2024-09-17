import { createBrowserRouter } from "react-router-dom";

import { HomePage } from "./pages/Home";
import { PublicPage } from "./pages/Public";
import { PrivatePage } from "./pages/Private";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <HomePage />,
  },
  {
    path: "/public",
    element: <PublicPage />,
  },
  {
    path: "/private",
    element: <PrivatePage />,
  },
]);
