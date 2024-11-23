import { Flex, Button, Link } from "@chakra-ui/react";

import {
  FaHouse,
  FaUser,
  FaGear,
  FaRegFaceKissWinkHeart,
} from "react-icons/fa6";

export function SideMenu({}) {
  return (
    <Flex
      height="100%"
      minWidth={{ base: "25vw", md: "20vw", lg: "15vw" }}
      direction="column"
    >
      <MenuItem to="#" icon={<FaHouse />}>
        Home
      </MenuItem>
      <MenuItem to="#profile" icon={<FaUser />}>
        Profile
      </MenuItem>
      <MenuItem to="#settings" icon={<FaGear />}>
        Settings
      </MenuItem>
      <MenuItem to="#etc" icon={<FaRegFaceKissWinkHeart />}>
        etc.
      </MenuItem>
    </Flex>
  );
}

function MenuItem({
  to,
  icon,
  children,
}: {
  to?: string;
  icon?: React.ReactNode;
  children: React.ReactNode;
}) {
  return (
    <Button
      asChild
      variant="ghost"
      focusRing="none"
      width="100%"
      justifyContent="start"
    >
      <Link href={to} variant="plain" textDecoration="none">
        {icon}
        {children}
      </Link>
    </Button>
  );
}
