import { Card, Heading, Flex } from "@chakra-ui/react";
import { FaChartColumn } from "react-icons/fa6";

import { Item } from "@/types";

export function ListItem({ item }: { item: Item }) {
  return (
    <Card.Root variant="outline" flexDirection="row" flexGrow={1} size="md">
      <Flex p={4} align="center" justify="center">
        <FaChartColumn size={32} />
      </Flex>
      <Flex grow={1} direction="column">
        <Card.Body asChild>
          <Flex justify="center">
            <Heading as="h2" size="md">
              {item.name}
            </Heading>
          </Flex>
        </Card.Body>
      </Flex>
    </Card.Root>
  );
}
