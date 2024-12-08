import { Button, Input } from "@repo/ui";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <div className="w-full max-w-md space-y-8">
        <div className="text-center">
          <h1 className="text-4xl font-bold">Welcome</h1>
          <p className="mt-2 text-gray-600">Sign in to your account</p>
        </div>

        <form className="mt-8 space-y-6">
          <div className="space-y-4">
            <div>
              <Input
                type="email"
                placeholder="Email address"
                autoComplete="email"
                required
              />
            </div>
            <div>
              <Input
                type="password"
                placeholder="Password"
                autoComplete="current-password"
                required
              />
            </div>
          </div>

          <div className="flex items-center justify-between">
            <div className="flex items-center">
              <input
                id="remember-me"
                name="remember-me"
                type="checkbox"
                className="h-4 w-4 rounded border-gray-300"
              />
              <label
                htmlFor="remember-me"
                className="ml-2 text-sm text-gray-600"
              >
                Remember me
              </label>
            </div>

            <div className="text-sm">
              <a href="#" className="text-primary hover:text-primary/90">
                Forgot your password?
              </a>
            </div>
          </div>

          <div className="space-y-4">
            <Button className="w-full" size="lg">
              Sign in
            </Button>
            <Button variant="outline" className="w-full" size="lg">
              Sign up
            </Button>
          </div>
        </form>
      </div>
    </main>
  );
}
