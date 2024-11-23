import { VStack } from "@chakra-ui/react";

import { Item } from "@/types";

import { ListItem } from "./ListItem";

/** Renders an item list. */
export function ItemList({ items }: { items: Item[] }) {
  return (
    <VStack align="left" gap={4}>
      {items.map((item) => (
        <ListItem key={item.id} item={item} />
      ))}
    </VStack>
  );
}
