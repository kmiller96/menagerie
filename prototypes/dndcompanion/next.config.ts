import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: "standalone", // Allows usage with docker
};

export default nextConfig;
