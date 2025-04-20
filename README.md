# Personal website

This is the public repo where all the code to deploy my personal website is located. This page is built entirely with the python library [reflex](https://reflex.dev/) and deployed it a [Vercel app](https://vercel.com/). You can check it at https://osllogon.com.

## Install dependencies

To manage the dependencies this project uses [uv](https://docs.astral.sh/uv). Therefore, to install the required packages you just need to execute:

    uv sync

## Deploy

The deployment of this project is done with vercel. You can just check in the `.github/workflows/deploy.yaml` how it is set up. This workflow generates the frontend and then uploads it to Vercel through Vercel CLI. In order to that, it is needed to configure the following variables in the `settings/secrets/actions` of the GitHub repo:

- VERCEL_ORG_ID
- VERCEL_PROJECT_ID
- VERCEL_TOKEN

With these variables you can upload any folder to a Vercel project through:

    vercel --prod --yes --token $VERCEL_TOKEN

## Deploy offline

Deployment can also be done with Vercel CLI manually, so this has two stages. The first one would be to compile and create a frontend we can then upload to Vercel. For that, we have to execute the following command:

    reflex export --frontend-only --no-zip

This will create the version we need to upload inside a folder called `.web/`. Then, we can deploy with Vercel by command line. If you have not installed Vercel just execute:

    npm i -g vercel

Then, to upload the website to Vercel you just have to run the following:

    cd .web
    vercel --prod

All of this taking into account that a Vercel account has to be created previously. 