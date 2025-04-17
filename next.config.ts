import type { NextConfig } from "next";
import createMDX from "@next/mdx";
import prism from "remark-prism";
import type { Pluggable } from "unified";

const nextConfig: NextConfig = {
	pageExtensions: ["js", "jsx", "md", "mdx", "ts", "tsx"],
};

const withMDX = createMDX({
	// extension: /\.mdx?$/,
	extension: /\.(md|mdx)$/,
	options: {
		remarkPlugins: [prism as Pluggable],
	},
});

export default withMDX(nextConfig);
