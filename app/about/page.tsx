import Link from "next/link";

export default function AboutPage() {
  return (
    <div className="min-h-screen bg-[#fafafa] text-zinc-900 [background-image:radial-gradient(#d4d4d8_1px,transparent_1px)] [background-size:18px_18px]">
      <section className="mx-auto max-w-3xl px-5 py-24 sm:py-24">
        <Link
          href="/"
          className="mb-12 inline-flex text-sm font-medium text-zinc-500 transition hover:text-zinc-900"
        >
          ← 記事一覧へ戻る
        </Link>

        <article className="rounded-[2rem] border border-zinc-200 bg-white/85 px-6 py-10 shadow-sm backdrop-blur-sm sm:px-10 sm:py-14">
          <p className="mb-4 text-xs font-bold tracking-[0.25em] text-red-500">
            ABOUT
          </p>

          <div className="mb-16">
            <h1 className="text-4xl font-black leading-none tracking-tight sm:text-5xl">
              ザウェブとは
            </h1>
          </div>

          <div className="space-y-7 text-[17px] leading-[2.1] text-zinc-800 sm:text-lg sm:leading-[2.2]">
            <p>
              ザウェブは、検索・生活・AI・消費行動の変化を観測するメディアです。
            </p>

            <p>
              日々の検索ワードや話題の変化には、人の関心、悩み、行動の兆しが表れます。
              このサイトでは、そうした小さな変化を記録し、今どんな流れが起きているのかを整理していきます。
            </p>

            <p>
              ニュースを追うだけではなく、「なぜ今それが検索されているのか」
              「どんな生活の変化につながっているのか」を見ることを大切にしています。
            </p>

            <p>
              Pythonによる情報収集、AIによる整理、Next.jsによる公開を組み合わせ、
              小さく更新し続ける観測メディアとして運営しています。
            </p>
          </div>
        </article>
      </section>
    </div>
  );
}
