import type { NextConfig } from "next";
import createMDX from "@next/mdx";

const nextConfig: NextConfig = {
	turbopack: {
		rules: {
			"*.md": {
				loaders: ["@mdx-js/loader"],
				as: "*.js",
			},
		},
	},
};

const withMDX = createMDX();

export default withMDX(nextConfig);
