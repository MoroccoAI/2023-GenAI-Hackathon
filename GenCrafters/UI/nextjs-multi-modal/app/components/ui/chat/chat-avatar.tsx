import { Shell, User2 } from "lucide-react";
import Image from "next/image";

export default function ChatAvatar({ role }: { role: string }) {
  if (role === "user") {
    return (
      <div className="flex h-8 w-8 shrink-0 select-none items-center justify-center rounded-md border bg-background shadow">
        <User2 className="h-4 w-4" />
      </div>
    );
  }

  return (
    <div className="flex h-8 w-8 shrink-0 select-none items-center justify-center rounded-md border  text-white shadow">
      <Image
        className="rounded-md"
        src="/shifa.png"
        alt="Lion Logo"
        width={25}
        height={22}
        priority
      />
      {/* <Shell className="h-4 w-4" /> */}
    </div>
  );
}
