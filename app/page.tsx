import Link from "next/link";
import posts from "@/data/published_posts.json";

type Post = {
  title: string;
  slug: string;
  tags: string[];
  comment: string;
  keyword: string;
  trend_score: number;
  created_at: string;
};

export default function Home() {
  const publishedPosts = posts as Post[];

  return (
    <main className="min-h-screen bg-[#fafafa] text-zinc-900 [background-image:radial-gradient(#d4d4d8_1px,transparent_1px)] [background-size:18px_18px]">
      <section className="mx-auto max-w-3xl px-5 py-16 sm:py-24">
        <div className="mb-10 flex h-2 w-full overflow-hidden rounded-full">
          <div className="w-2/3 bg-red-500" />
          <div className="w-1/3 bg-yellow-400" />
        </div>

        <header className="mb-16 border-b border-zinc-200 pb-10">
          <p className="mb-3 text-xs font-semibold tracking-[0.25em] text-zinc-500">
            THE WEB / OBSERVATION LOG
          </p>

          <h1 className="text-4xl font-bold tracking-tight sm:text-5xl">
            ザウェブ
          </h1>

          <p className="mt-5 leading-8 text-zinc-600">
            検索の空気、ツールの変化、Webまわりの小さな違和感を観測するメディアログ。
          </p>
        </header>

        <div className="flex flex-col gap-16">
          {publishedPosts.map((post, index) => (
            <article
              key={`${post.keyword}-${post.created_at}-${index}`}
              className="border-b border-zinc-300 bg-white/75 px-6 py-10 shadow-sm backdrop-blur-sm sm:px-8"
            >
              <div className="mb-5 flex flex-wrap items-center gap-3 text-xs text-zinc-500">
                <time>{post.created_at}</time>

                {post.tags?.length > 0 && (
                  <div className="flex flex-wrap gap-2">
                    {post.tags.map((tag) => (
                      <span key={tag} className="text-zinc-500">
                        #{tag}
                      </span>
                    ))}
                  </div>
                )}
              </div>

              <Link href={`/posts/${post.slug}`} className="group block">
                <h2 className="mb-5 text-3xl font-black leading-tight tracking-tight transition-opacity group-hover:opacity-70 sm:text-4xl">
                  {post.title}
                </h2>
              </Link>

              <p className="line-clamp-4 text-[15px] leading-8 text-zinc-600 sm:text-base">
                {post.comment}
              </p>

              <Link
                href={`/posts/${post.slug}`}
                className="mt-6 inline-block text-sm font-semibold text-zinc-900 underline decoration-red-400 decoration-2 underline-offset-4 transition hover:opacity-70"
              >
                観測ログを読む →
              </Link>

              <div className="mt-8 flex flex-wrap gap-3 text-xs text-zinc-400">
                <span>keyword: {post.keyword}</span>
                <span>score: {post.trend_score}</span>
              </div>
            </article>
          ))}
        </div>
      </section>
    </main>
  );
}