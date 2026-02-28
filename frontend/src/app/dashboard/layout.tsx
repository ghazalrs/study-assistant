import type { Metadata } from "next"
import "./globals.css"
import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar"
import { AppSidebar } from "@/components/app-sidebar"
import { TooltipProvider } from "@/components/ui/tooltip"

export const metadata: Metadata = {
  title: "Study Assistant"
}

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <SidebarProvider>
          <AppSidebar />
          <main className="flex flex-1 flex-col">
            <header className="flex h-14 items-center border-b px-4">
              <SidebarTrigger />
            </header>
            <TooltipProvider>
              <div className="flex-1 p-6">{children}</div>
            </TooltipProvider>
          </main>
        </SidebarProvider>
      </body>
    </html>
  )
}