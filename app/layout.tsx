import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import Footer from "./components/Footer";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  metadataBase: new URL("https://theweb.h3incover.com/"),

  title: {
    default: "ザウェブ | 生活変化・検索変化の観測メディア",
    template: "%s | ザウェブ",
  },

  description:
    "検索・生活・AI・消費行動の変化を観測するメディア。今、人は何を調べ、何に反応し、どんな行動へ向かっているのかを記録する。",

  keywords: [
    "AI",
    "検索トレンド",
    "生活変化",
    "Google Trends",
    "観測メディア",
    "Webメディア",
    "生成AI",
    "Claude",
    "ChatGPT",
  ],

  authors: [{ name: "H3 Incover" }],

  creator: "H3 Incover",

  openGraph: {
    type: "website",
    locale: "ja_JP",
    url: "https://theweb.h3incover.com/",
    siteName: "ザウェブ",

    title: "ザウェブ | 生活変化・検索変化の観測メディア",

    description: "検索・生活・AI・消費行動の変化を観測するメディア。",

    images: [
      {
        url: "/ogp.jpg",
        width: 1200,
        height: 630,
        alt: "ザウェブ",
      },
    ],
  },

  twitter: {
    card: "summary_large_image",
    title: "ザウェブ",
    description: "検索・生活・AI・消費行動の変化を観測するメディア。",
    images: ["/ogp.jpg"],
  },

  icons: {
    icon: "/favicon.ico",
    shortcut: "/favicon.ico",
    apple: "/apple-touch-icon.png",
  },

  robots: {
    index: true,
    follow: true,
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="ja"
      className={`${geistSans.variable} ${geistMono.variable} h-full antialiased`}
    >
      <body className="min-h-full flex flex-col bg-white text-zinc-900">
        <main className="flex-1">{children}</main>

        <Footer />
      </body>
    </html>
  );
}
