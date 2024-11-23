import { Box, BoxProps, Flex } from "@chakra-ui/react";

const PaddedBox = (props: BoxProps) => <Box px={3} py={3} {...props} />;

export function Layout({
  children,
}: {
  children: [React.ReactNode, React.ReactNode];
}) {
  const [sidebar, main] = children;

  return (
    <Flex h="100vh">
      <PaddedBox bg="blue.100">{sidebar}</PaddedBox>
      <PaddedBox flexGrow={1} bg="red.100">
        {main}
      </PaddedBox>
    </Flex>
  );
}
