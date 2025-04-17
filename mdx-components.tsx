import type { MDXComponents } from "mdx/types";

// export function useMDXComponents(components: MDXComponents): MDXComponents {
// 	return {
// 		h1: ({ children }) => <h1 className="font-bold text-5xl">{children}</h1>,
// 		...components,
// 	};
// }

export function useMDXComponents(components: MDXComponents): MDXComponents {
	return {
		h1: ({ children }) => <h1 className="text-2xl font-bold">{children}</h1>,
		h2: ({ children }) => <h1 className="text-xl font-bold">{children}</h1>,
		code: ({ children }) => <code className="whitespace-pre-wrap">{children}</code>,
		...components,
	};
}
