import { VStack, For, Link } from "@chakra-ui/react";

import { Item } from "@/types";

import { ListItem } from "./ListItem";

/** Renders an item list. */
export function ItemList({ items }: { items: Item[] }) {
  return (
    <VStack align="left" gap={4}>
      <For each={items}>
        {(item) => (
          <Link href={`/question/${item.id}`}>
            <ListItem key={item.id} item={item} />
          </Link>
        )}
      </For>
    </VStack>
  );
}
