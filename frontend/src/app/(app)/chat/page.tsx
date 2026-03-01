"use client"

import { useRef, useState, useEffect } from "react"
import { ArrowUp } from "lucide-react"
import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"

type Citation = { file: string; page: number; chunk_id: string }
type Message = { role: "user" | "assistant"; content: string; citations?: Citation[] }

const SUGGESTIONS = [
  "What are the main topics in this course?",
  "Summarize the lecture notes from week 1",
  "When is the midterm exam?",
  "What is the late submission policy?",
]

const API_BASE = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000"

export default function ChatPage() {
  const [messages, setMessages] = useState<Message[]>([])
  const [input, setInput] = useState("")
  const [loading, setLoading] = useState(false)
  const bottomRef = useRef<HTMLDivElement>(null)
  const textareaRef = useRef<HTMLTextAreaElement>(null)

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" })
  }, [messages])

  async function submit(question: string) {
    if (!question.trim() || loading) return

    setMessages((prev) => [...prev, { role: "user", content: question }])
    setInput("")
    setLoading(true)

    try {
      const res = await fetch(`${API_BASE}/rag/query`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
      })
      if (!res.ok) throw new Error()
      const data = await res.json()
      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: data.answer, citations: data.citations ?? [] },
      ])
    } catch {
      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: "Something went wrong. Is the backend running?" },
      ])
    } finally {
      setLoading(false)
      textareaRef.current?.focus()
    }
  }

  function handleKeyDown(e: React.KeyboardEvent<HTMLTextAreaElement>) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault()
      submit(input)
    }
  }

  return (
    <div className="flex flex-col h-[calc(100svh-3.5rem)]">

      {/* Messages / empty state */}
      <div className="flex-1 overflow-y-auto">
        {messages.length === 0 ? (
          <div className="flex flex-col items-center justify-center h-full gap-6 px-4">
            <div className="text-center space-y-2">
              <h1 className="text-3xl font-semibold tracking-tight">How can I help you today?</h1>
            </div>

            <div className="grid grid-cols-2 gap-2 w-full max-w-xl">
              {SUGGESTIONS.map((s) => (
                <button
                  key={s}
                  onClick={() => submit(s)}
                  className="text-sm text-left rounded-xl border bg-card px-4 py-3 hover:bg-accent transition-colors"
                >
                  {s}
                </button>
              ))}
            </div>
          </div>
        ) : (
          <div className="max-w-2xl mx-auto px-4 py-8 space-y-6">
            {messages.map((msg, i) => (
              <div key={i} className={`flex ${msg.role === "user" ? "justify-end" : "justify-start"}`}>
                <div
                  className={`max-w-[80%] rounded-2xl px-4 py-3 text-sm ${
                    msg.role === "user"
                      ? "bg-primary text-primary-foreground"
                      : "bg-muted text-foreground"
                  }`}
                >
                  <p className="whitespace-pre-wrap">{msg.content}</p>
                  {msg.citations && msg.citations.length > 0 && (
                    <div className="mt-3 pt-3 border-t border-border/40 space-y-1">
                      <p className="text-xs font-medium opacity-70">Sources</p>
                      {msg.citations.map((c, j) => (
                        <p key={j} className="text-xs opacity-60">
                          {c.file} — p.{c.page}
                        </p>
                      ))}
                    </div>
                  )}
                </div>
              </div>
            ))}

            {loading && (
              <div className="flex justify-start">
                <div className="bg-muted rounded-2xl px-4 py-3 text-sm text-muted-foreground">
                  <span className="animate-pulse">Thinking…</span>
                </div>
              </div>
            )}

            <div ref={bottomRef} />
          </div>
        )}
      </div>

      {/* Input bar */}
      <div className="shrink-0 border-t bg-background px-4 py-4">
        <div className="max-w-2xl mx-auto">
          <div className="relative flex items-end gap-2 rounded-2xl border bg-background px-4 py-3 shadow-sm focus-within:ring-1 focus-within:ring-ring">
            <Textarea
              ref={textareaRef}
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder="Send a message…"
              disabled={loading}
              rows={1}
              className="flex-1 resize-none border-0 bg-transparent dark:bg-transparent p-0 shadow-none focus-visible:ring-0 text-sm min-h-[1.5rem] max-h-40"
            />
            <Button
              size="icon"
              onClick={() => submit(input)}
              disabled={loading || !input.trim()}
              className="size-8 rounded-full shrink-0"
            >
              <ArrowUp className="size-4" />
            </Button>
          </div>
        </div>
      </div>
    </div>
  )
}
