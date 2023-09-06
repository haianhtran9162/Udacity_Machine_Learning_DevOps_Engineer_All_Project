#!/usr/bin/env python
"""
Download from W&B the raw dataset and apply some basic data cleaning, exporting the result to a new artifact
"""
import os
import argparse
import logging
import wandb
import pandas as pd


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(job_type="basic_cleaning")
    run.config.update(args)

    # Fetching the data
    logger.info("Fetching the artifact.")
    local_path = wandb.use_artifact(args.input_artifact).file()
    df = pd.read_csv(local_path)
    
    # Drop the outliers
    logger.info("Drop the outliers of the data.")
    min_price = args.min_price
    max_price = args.max_price
    idx = df['price'].between(min_price, max_price)
    df = df[idx].copy()
    
    # Convert last_review to datetime
    logger.info("Converting last_review to datetime.")
    df['last_review'] = pd.to_datetime(df['last_review'])
    
    # Filter longitude and latitude boundaries in and around NYC 
    # NOTE: Error become after release ver 1.0.0 -> 1.0.1
    idx = df['longitude'].between(-74.25, -73.50) & df['latitude'].between(40.5, 41.2)
    df = df[idx].copy()

    # Save the data cleanly
    logger.info("Saving the output data of artifact")
    df.to_csv(args.output_artifact, index=False)
    
    # Upload to the wandb
    artifact = wandb.Artifact(
        args.output_artifact,
        type=args.output_type,
        description=args.output_description,
    )
    artifact.add_file(args.output_artifact)
    run.log_artifact(artifact)
    
    os.remove(args.output_artifact)
    
    
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="A very basic data cleaning")


    parser.add_argument(
        "--input_artifact", 
        type=str,
        help="Name of the input artifact.",
        required=True
    )

    parser.add_argument(
        "--output_artifact", 
        type=str,
        help="Name of the output artifact.",
        required=True
    )

    parser.add_argument(
        "--output_type", 
        type=str,
        help="Type of the output artifact.",
        required=True
    )

    parser.add_argument(
        "--output_description", 
        type=str,
        help="Description of the output artifact.",
        required=True
    )

    parser.add_argument(
        "--min_price", 
        type=float,
        help="Minimum price for the clear outliers step.",
        required=True
    )

    parser.add_argument(
        "--max_price", 
        type=float,
        help="Maximum price for the clear outliers step.",
        required=True
    )


    args = parser.parse_args()

    go(args)
