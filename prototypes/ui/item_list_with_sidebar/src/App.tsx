import { useData } from "./hooks";

import { Layout } from "./Layout";
import { ItemList } from "./components/ItemList";

export default function App() {
  const { data } = useData();

  return (
    <Layout>
      <ItemList items={data} />
    </Layout>
  );
}
