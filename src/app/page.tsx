import Image from "next/image";

import Readme from "./../../README.mdx";

export default function Home() {
	return (
		<div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen gap-16 font-[family-name:var(--font-geist-sans)] max-w-[600px] w-[600px] whitespace-pre-wrap break-words">
			<main className="flex flex-col gap-4 row-start-2 items-center sm:items-start w-[600px] whitespace-pre-wrap break-words">
				<Readme />

				<div className="flex gap-4 items-center flex-col sm:flex-row">
					<a
						className="rounded-full border border-solid border-transparent transition-colors flex items-center justify-center bg-foreground text-background gap-2 hover:bg-[#383838] dark:hover:bg-[#ccc] font-medium text-sm sm:text-base h-10 sm:h-12 px-4 sm:px-5 sm:w-auto"
						href="https://github.com/Jish2/leetpals/edit/main/sites.yaml"
						target="_blank"
						rel="noopener noreferrer"
					>
						<Image className="invert dark:invert-0" src="/github-mark.svg" alt="github logomark" width={20} height={20} />
						join our webring
					</a>
				</div>
			</main>
			<footer className="row-start-3 flex gap-[24px] flex-wrap items-center justify-center">
				<a
					className="flex items-center gap-2 hover:underline hover:underline-offset-4"
					href="https://github.com/Jish2/leetpals?tab=readme-ov-file#leetpals-webring"
					target="_blank"
					rel="noopener noreferrer"
				>
					<Image aria-hidden src="/github-mark.svg" alt="File icon" width={16} height={16} />
					github
				</a>
				<a
					className="flex items-center gap-2 hover:underline hover:underline-offset-4"
					href="https://en.wikipedia.org/wiki/Webring#:~:text=A%20webring%20(or%20web%20ring,and%20often%20educational%20or%20social"
					target="_blank"
					rel="noopener noreferrer"
				>
					<Image aria-hidden src="/globe.svg" alt="Globe icon" width={16} height={16} />
					webring
				</a>
			</footer>
		</div>
	);
}
