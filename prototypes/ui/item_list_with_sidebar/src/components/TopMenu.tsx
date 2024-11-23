import { HStack } from "@chakra-ui/react";
import { AppTitle } from "./AppTitle";

export function TopMenu() {
  return (
    <HStack justify="center" py={4}>
      <AppTitle />
    </HStack>
  );
}
