import type { NextConfig } from "next";
import createMDX from "@next/mdx";
import prism from "remark-prism";

const nextConfig: NextConfig = {
	pageExtensions: ["js", "jsx", "md", "mdx", "ts", "tsx"],
};

const withMDX = createMDX({
	// extension: /\.mdx?$/,
	extension: /\.(md|mdx)$/,
	options: {
		// @ts-expect-error who knows
		remarkPlugins: [prism],
	},
});

export default withMDX(nextConfig);
