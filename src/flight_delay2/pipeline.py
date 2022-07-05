from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (
    select_cols,
    feature_engineering,
    make_pyspark_pipeline,
    split_data,
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=select_cols,
                inputs=["flights", "parameters"],
                outputs="flights_reduced",
                name="select_cols",
            ),
        ]
            )

