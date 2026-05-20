import Link from "next/link";

export default function Footer() {
  return (
    <footer className="mt-24 border-t border-zinc-800 bg-zinc-950 text-white">
      <div className="mx-auto flex max-w-6xl flex-col gap-12 px-6 py-12 md:flex-row md:items-start md:justify-between">

        {/* 左側 */}
        <div className="max-w-md">
          <p className="mb-3 text-sm font-semibold tracking-[0.2em] text-zinc-500">
            THE WEB
          </p>

          <h2 className="mb-4 text-2xl font-bold leading-tight text-zinc-900">
            検索と生活変化を、観測する。
          </h2>

          <p className="text-sm leading-7 text-zinc-600">
            AI・検索・生活・消費行動の変化を観測し、
            小さな違和感や変化の兆候を記録するメディア。
          </p>
        </div>

        {/* 右側 */}
        <div className="flex flex-col gap-4 text-sm text-zinc-600">
          <Link
            href="/about"
            className="transition hover:text-zinc-900"
          >
            About
          </Link>

          <a
            href="https://github.com/"
            target="_blank"
            rel="noopener noreferrer"
            className="transition hover:text-zinc-900"
          >
            GitHub
          </a>

          <a
            href="https://h3incover.com/"
            target="_blank"
            rel="noopener noreferrer"
            className="transition hover:text-zinc-900"
          >
            H3 Incover
          </a>
        </div>
      </div>

      <div className="border-t border-zinc-100">
        <div className="mx-auto flex max-w-6xl flex-col gap-2 px-6 py-5 text-xs text-zinc-500 sm:flex-row sm:items-center sm:justify-between">
          <p>© 2026 THE WEB</p>

          <p>Built with Next.js + Python + Vercel</p>
        </div>
      </div>
    </footer>
  );
}