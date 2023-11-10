# An example app for canonical redirects

This is an example application to show how to use the [Simplifier.net Resolve URL](https://simplifier.net/resolve) to make your FHIR canonicals resolve in the browser.

Note that this is just an example of how it can be done. You can implement the redirection in any lan guage or technique, based on your available infrastructure and canonical URL structure.

All that is required right now is that you maintain some configuration which canonical URLs should be resolved in which scope (FHIR package or project) and pass this on to Simplifier.

## Demo

See https://fake-acme.org for a demonstration based on the [ACME Corp Simplifier demo organization](https://simplifier.net/organization/acme).

## Running Locally

```bash
npm i -g vercel
vercel dev
```

Your Flask application is now available at `http://localhost:3000`.

## One-Click Deploy

This example is deployed with [Vercel](https://vercel.com) and based on [this example app](https://github.com/vercel/examples/tree/main/python/flask3).

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fexamples%2Ftree%2Fmain%2Fpython%2Fflask3&demo-title=Flask%203%20%2B%20Vercel&demo-description=Use%20Flask%203%20on%20Vercel%20with%20Serverless%20Functions%20using%20the%20Python%20Runtime.&demo-url=https%3A%2F%2Fflask3-python-template.vercel.app%2F&demo-image=https://assets.vercel.com/image/upload/v1669994156/random/flask.png)
