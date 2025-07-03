from argparse import ArgumentTypeError
from app.models import Arguments
import argparse


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    parser.add_argument("--where", required=False)
    parser.add_argument("--aggregate", required=False)
    args = parser.parse_args()
    if args.file is None:
        raise ArgumentTypeError("filename can`t be empty")

    return Arguments(args.file, args.where, args.aggregate)
