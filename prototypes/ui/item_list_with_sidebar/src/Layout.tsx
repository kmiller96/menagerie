import { Flex, FlexProps } from "@chakra-ui/react";

import { SideMenu } from "./components/SideMenu";
import { TopMenu } from "./components/TopMenu";

const PaddedFlex = (props: FlexProps) => <Flex px={3} py={3} {...props} />;

export function Layout({ children }: { children: React.ReactNode }) {
  return (
    <Flex height="100vh" direction="column" overflowY="hidden">
      <Flex
        borderBottomWidth={1}
        borderBottomStyle="solid"
        borderBottomColor="colorPalette.100"
      >
        <TopMenu />
      </Flex>
      <Flex grow={1} dir="row" overflowY="scroll">
        <PaddedFlex
          borderRightWidth={1}
          borderRightStyle="solid"
          borderRightColor="colorPalette.100"
        >
          <SideMenu />
        </PaddedFlex>
        <PaddedFlex flexGrow={1} direction="column" overflowY="scroll">
          {children}
        </PaddedFlex>
      </Flex>
    </Flex>
  );
}
