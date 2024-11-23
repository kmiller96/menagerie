import { Flex, FlexProps } from "@chakra-ui/react";

import { SideMenu } from "./components/SideMenu";
import { TopMenu } from "./components/TopMenu";

const PaddedFlex = (props: FlexProps) => <Flex px={3} py={3} {...props} />;

export function Layout({ children }: { children: React.ReactNode }) {
  return (
    <Flex h="100vh" direction="column">
      <Flex
        borderBottomWidth={1}
        borderBottomStyle="solid"
        borderBottomColor="colorPalette.100"
      >
        <TopMenu />
      </Flex>
      <Flex grow={1} dir="row">
        <PaddedFlex
          borderRightWidth={1}
          borderRightStyle="solid"
          borderRightColor="colorPalette.100"
        >
          <SideMenu />
        </PaddedFlex>
        <PaddedFlex flexGrow={1} direction="column">
          {children}
        </PaddedFlex>
      </Flex>
    </Flex>
  );
}
